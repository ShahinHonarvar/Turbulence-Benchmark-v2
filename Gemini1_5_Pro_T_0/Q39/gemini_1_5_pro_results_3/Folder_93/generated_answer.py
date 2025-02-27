def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) >= sorted(list({ord(char) for char in text}), reverse=True)[76]], reverse=True)