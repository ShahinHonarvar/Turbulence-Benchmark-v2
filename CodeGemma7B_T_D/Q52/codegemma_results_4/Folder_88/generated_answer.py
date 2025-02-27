def palindrome_of_length_n(str):
    return {(str[i:i + 13].lower(), str[i + 1:i + 14].lower()) for i in range(len(str) - 13 + 1) if str[i:i + 13].lower() == str[i + 1:i + 14].lower()}