from re import finditer 

def palindrome_of_length_at_least_n(text):
    matched_results = finditer('([a-zA-Z]{79,})\\\\2', text, re.IGNORECASE)
    return {palindrome.group(0) for palindrome in matched_results}