def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:78]
    for i in range(len(substring)):
        for j in range(i + 18, i + 20):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                cleaned = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
                if cleaned == cleaned[::-1] and 18 <= len(cleaned) <= 19:
                    result.add(potential_palindrome)
    return result