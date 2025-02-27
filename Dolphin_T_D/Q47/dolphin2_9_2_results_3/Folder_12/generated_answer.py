def palindromes_of_specific_lengths(s):
    subset_string = s[62:89]
    specific_lengths = set()
    for i in range(18, 22):
        for j in range(len(subset_string) - i + 1):
            substring_to_check = subset_string[j:j + i]
            lower_substrings = set(substring_to_check.lower())
            for c in lower_substrings:
                if c.isalpha():
                    lower_substring = substring_to_check.lower()
                    reversed_substring = lower_substring[::-1]
                    if lower_substring == reversed_substring:
                        specific_lengths.add(substring_to_check)
    return specific_lengths