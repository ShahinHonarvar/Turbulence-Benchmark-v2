def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[10:76]
    substr = ''.join((c.lower() for c in substr if c.isalpha()))
    for i in range(len(substr)):
        for j in range(i + 10, min(i + 21, len(substr) + 1)):
            if j - i > 20:
                break
            segment = substr[i:j]
            if segment == segment[::-1]:
                result.add(segment)
    return result