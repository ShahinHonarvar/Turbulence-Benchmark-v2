def palindrome_of_length_n(input_string, length=21):
    valid_palindromes = set()
    for i in range(len(input_string) - length + 1):
        current_substring = input_string[i:i + length]
        if current_substring.lower() == current_substring.lower()[::-1] and current_substring.isalpha():
            valid_palindromes.add(current_substring)
    return valid_palindromes