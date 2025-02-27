from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    relevant_string = ''.join([char for char in string[:6] if char in letters])
    char_counts = Counter(relevant_string)
    palindromes = set()
    for perm in permutations(relevant_string):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            word_char_counts = Counter(word)
            is_palindrome = True
            for char in word_char_counts:
                if char_counts[char] < word_char_counts[char]:
                    is_palindrome = False
                    break
            if is_palindrome:
                palindromes.add(word)
    return palindromes