def palindromes_of_specific_lengths(s):
    substring = s[17:73]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 50, i + 52):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                cleaned = ''.join((c for c in potential_palindrome if c.isalpha()))
                if cleaned == cleaned[::-1] and 50 <= len(cleaned) <= 51:
                    result.add(cleaned.lower())
    return result