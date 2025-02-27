def palindrome_of_length_n(input_string, n=401):
    input_string = ''.join((e for e in input_string if e.isalpha())).lower()
    if len(input_string) < n:
        return set()
    palindromes = {input_string[i:i + n] for i in range(len(input_string) - n + 1) if input_string[i:i + n] == input_string[i:i + n][::-1]}
    return palindromes