def palindromes_of_specific_lengths(s):
    substring = s[31:92]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 50, min(i + 54, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome.lower() if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 50 <= len(cleaned_palindrome) <= 53:
                result.add(potential_palindrome)
    return result