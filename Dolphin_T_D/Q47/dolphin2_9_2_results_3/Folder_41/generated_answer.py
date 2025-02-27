def palindromes_of_specific_lengths(s):
    lowercase_s = s.lower()
    relevant_substring = lowercase_s[1:8]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(relevant_substring) - length + 1):
            element = relevant_substring[i:i + length]
            if element == element[::-1] and element.isalpha():
                palindromes.add(element)
    return palindromes