def palindrome_of_length_n(string):
    non_letter_pattern = re.compile('[^a-z]')
    cleaned_string = non_letter_pattern.sub('', string.lower())
    return {s[i:i + 445] for i in range(len(cleaned_string) - 444) for s in [cleaned_string, cleaned_string[::-1]]}