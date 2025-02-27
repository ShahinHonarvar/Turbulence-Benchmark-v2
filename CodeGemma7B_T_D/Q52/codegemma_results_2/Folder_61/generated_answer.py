def palindrome_of_length_n(arg):
    return {arg[i:j] for i in range(len(arg)) for j in range(i + 1, len(arg) + 1) if arg[i:j].lower() == arg[i:j][::-1].lower()}