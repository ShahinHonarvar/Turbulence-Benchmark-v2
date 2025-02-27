from collections import defaultdict, Counter

def palindromes_between_indices(string):
    pairs = defaultdict(set)
    pairs['a'].update(['a', 'A'])
    pairs['b'].update(['b', 'B'])
    pairs['c'].update(['c', 'C'])
    pairs['d'].update(['d', 'D'])
    pairs['e'].update(['e', 'E'])
    pairs['f'].update(['f', 'F'])
    pairs['g'].update(['g', 'G'])
    pairs['h'].update(['h', 'H'])
    pairs['i'].update(['i', 'I'])
    pairs['j'].update(['j', 'J'])
    pairs['k'].update(['k', 'K'])
    pairs['l'].update(['l', 'L'])
    pairs['m'].update(['m', 'M'])
    pairs['n'].update(['n', 'N'])
    pairs['o'].update(['o', 'O'])
    pairs['p'].update(['p', 'P'])
    pairs['q'].update(['q', 'Q', '0'])
    pairs['r'].update(['r', 'R'])
    pairs['s'].update(['s', 'S'])
    pairs['t'].update(['t', 'T'])
    pairs['u'].update(['u', 'U'])
    pairs['v'].update(['v', 'V'])
    pairs['w'].update(['w', 'W'])
    pairs['x'].update(['x', 'X'])
    pairs['y'].update(['y', 'Y'])
    pairs['z'].update(['z', 'Z'])
    character_count = Counter(string)
    palindromes = set()
    for letter in character_count:
        if letter in pairs:
            for i in range(character_count[letter]):
                for j in range(i + 1, character_count[letter]):
                    for k in range(j + 1, character_count[letter]):
                        if letter * 3 == pairs['a'][i] + pairs['b'][j] + pairs['c'][k]:
                            palindromes.add(pairs['a'][i] + pairs['b'][j] + pairs['c'][k])
    return palindromes