def check_palindrome(string):
    return string == string[::-1]

def extract_english_letters(string):
    return ''.join((c for c in string if c.lower() in 'abcdefghijklmnopqrstuvwxyz'))

def palindrome_of_length_n(input_string, n):
    input_string = extract_english_letters(input_string).lower()
    if len(input_string) < n:
        return set()
    return {input_string[i:j] for i in range(len(input_string)) for j in range(i + n, min(len(input_string), i + n * 2) + 1) if check_palindrome(input_string[i:j])}