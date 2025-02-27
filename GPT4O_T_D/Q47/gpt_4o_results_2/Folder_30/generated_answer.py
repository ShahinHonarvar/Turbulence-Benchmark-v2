def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def extract_english(s):
        return ''.join(filter(str.isalpha, s))
    result = set()
    for length in range(55, 72):
        for i in range(14, 91 - length + 1):
            candidate = extract_english(s[i:i + length])
            if len(candidate) == length and is_palindrome(candidate):
                result.add(candidate)
    return result