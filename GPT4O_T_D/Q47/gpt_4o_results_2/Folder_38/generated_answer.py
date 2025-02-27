import re

def palindromes_of_specific_lengths(s):
    substr = s[18:88]
    cleaned_substr = re.sub('[^a-zA-Z]', '', substr)
    palindromes = set()
    for i in range(len(cleaned_substr)):
        for j in range(i + 38, min(i + 61, len(cleaned_substr) + 1)):
            candidate = cleaned_substr[i:j]
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes