def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[155:284]
    for i in range(len(substring) - 103):
        for j in range(i + 104, min(i + 121, len(substring)) + 1):
            palindrome = substring[i:j]
            if palindrome.isalpha() and palindrome.lower() == palindrome.lower()[::-1]:
                result.add(palindrome)
    return result