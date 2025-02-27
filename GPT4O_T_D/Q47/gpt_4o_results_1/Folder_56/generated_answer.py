def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    substring = s[1:10]
    lower_substring = ''.join(filter(str.isalpha, substring.lower()))
    n = len(lower_substring)
    for length in range(3, 8):
        for i in range(n - length + 1):
            candidate = lower_substring[i:i + length]
            if candidate == candidate[::-1]:
                valid_palindromes.add(candidate)
    return valid_palindromes