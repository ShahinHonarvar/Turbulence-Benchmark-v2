import re
  from collections import Counter

def palindromes_between_indices(string):
    letters = re.sub('[^a-zA-Z]', '', string[4:9])
    letters_count = Counter(letters.lower())
    odd_counts = [l for l in letters_count if letters_count[l] % 2 != 0]
    palindromes = set()
    if len(letters) >= 3 and len(odd_counts) <= 1:
        middle = max(odd_counts, key=lambda item: letters_count[item], default='')
        half_palindrome = ''
        for letter in letters_count:
            if letter != middle:
                half_palindrome += letter * (letters_count[letter] // 2)
        perm_set = set()
        permutation_helper(list(half_palindrome), 0, len(half_palindrome) - 1, perm_set)
        for item in perm_set:
            palindromes.add(item + middle + item[::-1])
    return palindromes

def permutation_helper(string, left, right, perm_set):
    if left == right:
        perm_set.add(''.join(string))
    else:
        for i in range(left, right + 1):
            string[left], string[i] = (string[i], string[left])
            permutation_helper(string, left + 1, right, perm_set)
            string[left], string[i] = (string[i], string[left])