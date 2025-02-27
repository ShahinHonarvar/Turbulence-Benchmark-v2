def return_n_greatest_chars(input_string: str) -> list[str]:
    input_string = ''.join(sorted(input_string, key=lambda x: ord(x), reverse=True))
    return list(input_string[:28])