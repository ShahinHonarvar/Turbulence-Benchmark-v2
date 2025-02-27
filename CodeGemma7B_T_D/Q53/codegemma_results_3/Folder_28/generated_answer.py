def palindrome_of_length_at_least_n(s):
    results = set()
    for center in range(len(s)):
        for radius in range(center - 41, center + 42):
            if radius >= 0 and radius < len(s) and (s[center].lower() == s[radius].lower()):
                palindrome = s[radius:center + 1]
                results.add(palindrome)
    return results