import itertools

def palindromes_between_indices(s):
    letters = {char.lower() for char in s[4:6] if char.isalpha()}
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes