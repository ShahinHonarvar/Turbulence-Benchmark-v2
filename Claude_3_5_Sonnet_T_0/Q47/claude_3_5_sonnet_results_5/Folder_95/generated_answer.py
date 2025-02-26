def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 20, i + 22):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
                if 20 <= len(cleaned_palindrome) <= 21 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                    result.add(cleaned_palindrome)
    return result