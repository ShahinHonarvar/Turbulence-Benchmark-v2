def palindromes_of_specific_lengths(s):
    substring = s[17:73]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 50, i + 52):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
                if cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1] and 50 <= len(cleaned_palindrome) <= 51:
                    result.add(cleaned_palindrome)
    return result