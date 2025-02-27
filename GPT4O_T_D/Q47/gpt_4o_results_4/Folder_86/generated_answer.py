def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        cleaned_sub = ''.join((c for c in sub if c.isalpha())).lower()
        return cleaned_sub == cleaned_sub[::-1]
    result = set()
    for start in range(30, 96):
        for length in range(34, 56):
            end = start + length
            if end > 96:
                break
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring)
    return result