import re

def palindromes_of_specific_lengths(s):
    range_start, range_end = (18, 87)
    min_length, max_length = (38, 60)
    subset = re.sub('[^a-zA-Z]', '', s[range_start:range_end + 1])
    subset_lower = subset.lower()
    palindromes = set()
    for i in range(len(subset_lower)):
        for j in range(i + min_length, min(i + max_length, len(subset_lower)) + 1):
            sub = subset_lower[i:j]
            if sub == sub[::-1]:
                palindromes.add(subset[i:j])
    return palindromes