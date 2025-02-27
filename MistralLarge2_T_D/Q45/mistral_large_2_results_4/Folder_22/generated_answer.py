import itertools

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes