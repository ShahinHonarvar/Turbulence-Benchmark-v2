def palindromes_of_specific_lengths(string):
    letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return {palindrome.upper() for length in range(10, 37) for start in range(24, 98) for end in range(start, start + length) if end < 98 and string[end] in letters and (string[start:end + 1] == string[start:end + 1][::-1])}