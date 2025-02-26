def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:90]

    def is_palindrome(text):
        return text.lower() == text.lower()[::-1]
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 73, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome) and (40 <= len(potential_palindrome) <= 72):
                result.add(potential_palindrome)
    return result