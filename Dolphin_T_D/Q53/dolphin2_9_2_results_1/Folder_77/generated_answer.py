def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    output_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 148):
        for j in range(i + 149, len(input_string) + 1):
            sub_string = input_string[i:j]
            if all((c.isalpha() for c in sub_string)) and is_palindrome(sub_string):
                output_set.add(sub_string)
    return output_set