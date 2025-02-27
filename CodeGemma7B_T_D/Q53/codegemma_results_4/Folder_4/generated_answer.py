def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            if all((c.isalpha() for c in string[i:j])):
                if string[i:j] == string[i:j][::-1]:
                    result.add(string[i:j])