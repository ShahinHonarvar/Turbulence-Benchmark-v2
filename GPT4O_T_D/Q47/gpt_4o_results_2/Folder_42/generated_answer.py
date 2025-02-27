from re import sub

def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = sub('[^a-z]', '', s[43:96])
    palindromes = set()
    for length in range(18, 48):
        for start in range(len(substring) - length + 1):
            segment = substring[start:start + length]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes