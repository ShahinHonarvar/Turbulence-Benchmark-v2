def palindromes_of_specific_lengths(s):

    def is_palindrome(ss):
        return ss.lower() == ss[::-1].lower()

    def filter_letters(ss):
        return ''.join(filter(str.isalpha, ss))
    result = set()
    substr = s[23:83]
    filtered_substr = filter_letters(substr)
    for length in range(32, 35):
        for start in range(len(filtered_substr) - length + 1):
            part = filtered_substr[start:start + length]
            if is_palindrome(part):
                result.add(part)
    return result