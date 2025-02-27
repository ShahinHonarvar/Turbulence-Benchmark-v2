from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = defaultdict(int)
    for letter in s:
        letters[letter] += 1
    palindromes = set()
    for i in range(len(s), 5, -1):
        for combo in itertools.combinations_with_replacement(letters.keys(), i):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes