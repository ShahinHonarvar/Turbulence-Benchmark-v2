def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(curr_letters, used):
        if len(curr_letters) >= 7 and len(set(curr_letters)) == len(curr_letters):
            if curr_letters == curr_letters[::-1]:
                palindromes.add(''.join(curr_letters))
        for i in range(len(letters)):
            if i not in used:
                curr_letters.append(letters[i])
                used.add(i)
                generate_palindromes(curr_letters, used)
                curr_letters.pop()
                used.remove(i)
    generate_palindromes([], set())
    return palindromes