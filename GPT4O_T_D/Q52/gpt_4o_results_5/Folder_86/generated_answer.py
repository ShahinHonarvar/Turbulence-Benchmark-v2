def palindrome_of_length_n(s):
    normalized_string = ''.join((c for c in s if c.isalpha())).lower()
    length = len(normalized_string)
    palindromes = set()
    target_length = 181
    for i in range(length - target_length + 1):
        substr = normalized_string[i:i + target_length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes