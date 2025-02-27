def palindromes_of_specific_lengths(text):
    text = text[125:284]
    palindromes = set()
    for i in range(len(text) - 108):
        substring = text[i:i + 109]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 110]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 111]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 112]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 113]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 114]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 115]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 116]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 117]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 118]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 119]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 120]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 121]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 122]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 123]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 124]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 125]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
        substring = text[i:i + 126]
        if substring.lower() == substring.lower()[::-1] and 109 <= len(substring) <= 126:
            palindromes.add(substring)
    return palindromes