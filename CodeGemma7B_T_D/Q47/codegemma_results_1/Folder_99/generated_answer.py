def palindromes_of_specific_lengths(str):
    nodepalindromes = set()
    n = 127
    while n + 141 <= len(str):
        prefix = str[n:n + 119]
        suffix = str[n + 141:n + 288]
        set_current = find_nodepalindromes(prefix, suffix)
        nodepalindromes = nodepalindromes.union(set_current)
        n += 1
    result = set()
    for palindrome in nodepalindromes:
        if len(palindrome) >= 119 and len(palindrome) <= 141:
            result.add(palindrome)
    return result

def find_nodepalindromes(prefix, suffix):
    nodepalindromes = set()
    for i in range(len(prefix)):
        for j in range(len(suffix)):
            both_cases = prefix[i:] + suffix[j:]
            reverse_both_cases = both_cases[::-1]
            if both_cases == reverse_both_cases:
                nodepalindromes.add(lower_string(both_cases))
    return nodepalindromes

def lower_string(s):
    return ''.join([char.lower() if char.isalpha() else char for char in s])