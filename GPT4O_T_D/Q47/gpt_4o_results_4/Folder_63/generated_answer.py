def palindromes_of_specific_lengths(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    filtered_substring = ''.join((c for c in s[33:86] if c.isalpha()))
    found_palindromes = set()
    length_conditions = range(26, 32)
    for start in range(len(filtered_substring)):
        for length in length_conditions:
            end = start + length
            if end <= len(filtered_substring):
                substring = filtered_substring[start:end].lower()
                if is_palindrome(substring):
                    found_palindromes.add(substring)
    return found_palindromes