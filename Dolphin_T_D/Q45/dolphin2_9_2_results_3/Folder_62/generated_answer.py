def palindromes_between_indices(data):
    data = ''.join(sorted(list(filter(str.isalpha, data[:9]))))
    palindromes = set()

    def helper(palin, d):
        if len(palin) > 1:
            palindromes.add(''.join(palin))
        for i in range(len(d)):
            helper(palin + d[i].lower(), d[:i] + d[i + 1:])
    helper('', data)
    return palindromes