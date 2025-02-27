def filter_chars(text):
    filtered_text = ''.join([char for char in text if (ord(char) >= 57 and ord(char) <= 96) and char not in '<w'])
    return filtered_text