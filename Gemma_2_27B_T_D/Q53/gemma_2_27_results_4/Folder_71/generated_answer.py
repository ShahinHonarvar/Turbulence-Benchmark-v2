def palindrome_of_length_at_least_n(text):
    return {substring for substring in text.lower() for i in range(len(substring) - 86) if substring[i:i + 87] == substring[i:i + 87][::-1]}