def palindrome_of_length_n(text):
    filtered_text = ''.join(filter(str.isalpha, text))
    lowercase_text = filtered_text.lower()
    return {text[i:i + 338] for i in range(len(text) - 337)}