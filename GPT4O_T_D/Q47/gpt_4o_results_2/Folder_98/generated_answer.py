def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()

    def get_english_chars(subs):
        return ''.join(filter(str.isalpha, subs))
    limited_s = s[:21]
    result = set()
    for i in range(len(limited_s)):
        for j in range(i + 5, min(len(limited_s), i + 81)):
            candidate = limited_s[i:j + 1]
            filtered_candidate = get_english_chars(candidate)
            if len(filtered_candidate) >= 5 and is_palindrome(filtered_candidate):
                result.add(candidate)
    return result