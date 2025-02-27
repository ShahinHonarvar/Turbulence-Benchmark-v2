import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[2:9] if ch.isalpha()]
    lower_letters = [ch.lower() for ch in letters]
    palindromes = set()
    for length in range(7, len(lower_letters) + 1):
        for combination in itertools.combinations(lower_letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes