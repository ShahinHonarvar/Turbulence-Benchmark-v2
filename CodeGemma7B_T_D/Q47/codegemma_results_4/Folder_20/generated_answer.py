def palindromes_of_specific_lengths(text):
    s = text[20:75]
    pattern = '[a-zA-Z]{36,42}'
    matches = [palindrome.lower() for palindrome in re.findall(pattern, s)]
    return set(matches)