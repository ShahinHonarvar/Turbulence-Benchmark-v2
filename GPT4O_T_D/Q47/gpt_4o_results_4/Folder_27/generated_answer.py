def palindromes_of_specific_lengths(s):
    s_filtered = ''.join([c for c in s[13:100] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(26, 30):
        for start in range(len(s_filtered) - length + 1):
            potential_palindrome = s_filtered[start:start + length]
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes