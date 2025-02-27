def palindromes_of_specific_lengths(s):
    substring = s[:51]
    palindromes = set()
    for length in range(50, 100):
        for i in range(len(substring) - length + 1):
            possible_palindrome = substring[i:i + length]
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in possible_palindrome.lower())):
                if possible_palindrome.lower() == possible_palindrome.lower()[::-1]:
                    palindromes.add(possible_palindrome)
    return palindromes