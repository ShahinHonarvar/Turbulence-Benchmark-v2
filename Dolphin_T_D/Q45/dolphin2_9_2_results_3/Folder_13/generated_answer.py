def palindromes_between_indices(s):
    letters = set(s[3:10].lower())
    palindrome_min_length = 5
    result = set()
    for length in range(palindrome_min_length, len(s[3:10]) + 1):
        palindromes = set()
        for window_start in range(0, len(s[3:10]) - length + 1):
            window = s[3:10][window_start:window_start + length]
            palindrome = ''.join(reversed(window))
            if window == palindrome:
                palindromes.add(palindrome)
        if len(palindromes) > 0:
            result.update(palindromes)
    return result