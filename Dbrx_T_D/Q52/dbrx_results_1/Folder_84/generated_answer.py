def palindrome_of_length_n(input_string: str, target_length: int=131) -> set:
    if not isinstance(input_string, str) or not isinstance(target_length, int) or (not input_string) or (target_length <= 0):
        return set()
    allowed_characters = set(string.ascii_letters)
    input_string = ''.join((c for c in input_string.lower() if c in allowed_characters))
    if target_length > len(input_string) or target_length % 2 == 0:
        return set()
    palindromes = set()
    for i in range(len(input_string) - target_length + 1):
        substring = input_string[i:i + target_length]
        if len(substring) == target_length and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes