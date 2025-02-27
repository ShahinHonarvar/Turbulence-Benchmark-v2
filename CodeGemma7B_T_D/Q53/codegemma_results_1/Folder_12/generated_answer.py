def palindrome_of_length_at_least_n(text):
    pattern = re.compile('(?i)([A-Za-z]{51,})')
    return set(pattern.findall(text.lower()))