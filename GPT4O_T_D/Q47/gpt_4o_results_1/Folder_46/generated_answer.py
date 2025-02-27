def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    filtered_str = ''.join([c for c in s[11:98] if c.isalpha()])
    l = len(filtered_str)
    results = set()
    for length in range(29, 63):
        for start in range(l - length + 1):
            substring = filtered_str[start:start + length]
            if is_palindrome(substring):
                results.add(substring)
    return results